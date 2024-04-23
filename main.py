import psycopg2
import unittest


class TestPhoneCallDurations(unittest.TestCase):
    def setUp(self):
        self.conn = psycopg2.connect(
            dbname="testdb",
            user="postgres",
            password="mysecretpassword",
            host="localhost",
            port="5432"
        )
        self.cur = self.conn.cursor()

    def test_call_durations(self):
        self.cur.execute("""
        SELECT DISTINCT phones.name
        FROM phones
        JOIN (
            SELECT phone_number, SUM(duration) AS total_duration
            FROM (
                SELECT caller AS phone_number, duration FROM calls
                UNION ALL
                SELECT callee AS phone_number, duration FROM calls
            ) AS combined
            GROUP BY phone_number
            HAVING SUM(duration) > 10
        ) AS call_summary ON phones.phone_number = call_summary.phone_number;
        """)

        results = self.cur.fetchall()

        self.assertIn(('Alice',), results)
        self.assertIn(('Carol',), results)

        # Bob has called police for 3 minutes, therefore he should be in the
        # results (over 10 mins of calls) but the police should not
        self.assertIn(('Bob',), results)
        self.assertNotIn(('Police',), results)

    def tearDown(self):
        self.cur.close()
        self.conn.close()


if __name__ == '__main__':
    unittest.main()

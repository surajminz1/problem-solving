SELECT
    *
FROM
    final_table
QUALIFY ROW_NUMBER() OVER (
    PARTITION BY user_id
    ORDER BY event_ts DESC
) = 1
AND (amount < 0 OR status NOT IN ('success', 'pending');)
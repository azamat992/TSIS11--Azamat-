CREATE OR REPLACE FUNCTION get_records_by_pattern(pattern_text TEXT)
RETURNS SETOF your_table AS
$$
BEGIN
    RETURN QUERY SELECT * FROM your_table WHERE your_column ILIKE '%' || pattern_text || '%';
END;
$$
LANGUAGE plpgsql;

SELECT * FROM get_records_by_pattern('pattern');






-- 1. Each returned cohort must have exactly :q students.
SELECT result_no, COUNT(*) AS n
FROM dean_results
WHERE run_id = :run_id
GROUP BY result_no
HAVING COUNT(*) <> :q;
-- Must return zero rows.

-- 2. No cohort may contain an exclusion edge.
SELECT DISTINCT r1.result_no
FROM dean_results r1
JOIN dean_results r2
  ON r2.run_id = r1.run_id
 AND r2.result_no = r1.result_no
 AND r2.student_id > r1.student_id
JOIN exclusions e
  ON e.a = LEAST(r1.student_id,r2.student_id)
 AND e.b = GREATEST(r1.student_id,r2.student_id)
WHERE r1.run_id = :run_id;
-- Must return zero rows.

-- 3. Four results must be distinct. A compact check compares symmetric differences.
WITH pairs AS (
  SELECT a.result_no AS ra, b.result_no AS rb
  FROM (SELECT DISTINCT result_no FROM dean_results WHERE run_id=:run_id) a
  JOIN (SELECT DISTINCT result_no FROM dean_results WHERE run_id=:run_id) b
    ON a.result_no < b.result_no
), diff AS (
  SELECT p.ra,p.rb,COUNT(*) AS delta
  FROM pairs p
  JOIN (
    SELECT result_no,student_id FROM dean_results WHERE run_id=:run_id
  ) x ON x.result_no IN (p.ra,p.rb)
  GROUP BY p.ra,p.rb,x.student_id
  HAVING COUNT(*)=1
)
SELECT ra,rb,COUNT(*) FROM diff GROUP BY ra,rb HAVING COUNT(*)=0;
-- Must return zero rows.

CREATE TABLE students (
    student_id BIGINT PRIMARY KEY,
    payload JSONB
);

CREATE TABLE exclusions (
    a BIGINT NOT NULL REFERENCES students(student_id),
    b BIGINT NOT NULL REFERENCES students(student_id),
    CHECK (a < b),
    PRIMARY KEY (a,b)
);

CREATE INDEX exclusions_ba ON exclusions (b,a);

CREATE TABLE dean_results (
    run_id UUID NOT NULL,
    result_no SMALLINT NOT NULL CHECK (result_no BETWEEN 1 AND 4),
    student_id BIGINT NOT NULL REFERENCES students(student_id),
    PRIMARY KEY (run_id,result_no,student_id)
);

CREATE TABLE gyro_certificate_events (
    run_id UUID NOT NULL,
    seq BIGSERIAL,
    carrier TEXT NOT NULL,
    theorem TEXT NOT NULL,
    detail JSONB NOT NULL,
    PRIMARY KEY (run_id,seq)
);

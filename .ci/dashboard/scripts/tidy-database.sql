/*
fontspector will dump all run results into a database. We don't need
all that information, so we consolidate it into summary tables
*/
CREATE TABLE IF NOT EXISTS statuses_by_check (
    run TIMESTAMP,
    check_id VARCHAR,
    status ENUM('WARN', 'FAIL', 'ERROR'),
    status_count INTEGER,
    PRIMARY KEY (run, check_id, status)
);
CREATE TABLE IF NOT EXISTS statuses_by_family (
    run TIMESTAMP,
    family VARCHAR,
    status ENUM('WARN', 'FAIL', 'ERROR'),
    status_count INTEGER,
    PRIMARY KEY (run, family, status)
);
CREATE TABLE IF NOT EXISTS run_summary (
    run TIMESTAMP,
    status ENUM('WARN', 'FAIL', 'ERROR'),
    status_count INTEGER,
    PRIMARY KEY (run, status)
);

insert or ignore into statuses_by_check
select run, check_id, status, count(status) as status_count
from results
where status == 'FAIL' or status == 'ERROR' or status == 'WARN'
group by run, check_id, status;

insert or ignore into statuses_by_family
select run, directory as family, status, count(status) as status_count
    from results
    where status in ('WARN', 'FAIL', 'ERROR')
    group by run, family, status;

insert or ignore into run_summary
select run, status, count(status) as status_count
    from results
    where status in ('WARN', 'FAIL', 'ERROR')
    group by run, status;

/* Clean up the results table; keep only the latest run */

DELETE FROM results
WHERE run NOT IN (
    SELECT MAX(run) AS max_run
        FROM results
);
CHECKPOINT;

ATTACH 'fontspector-new.db' AS fontspectornew;
COPY FROM DATABASE fontspector TO fontspectornew;
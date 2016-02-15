# gofetch

Manage and execute query templates (Python and Hive for now)

# Usage

```sql
SELECT {{ fields }}
FROM {{ table }}
WHERE {{ conditions }}
;
```

```
gofetch template.sql \
       --table test.test \
       --fields b,c  \
       --where 'a > 1' --result a.csv'
```

The idea is to install `gofetch` (as in pip) and the conventioned directories will be created.

# Convention

```shell
--result specifies result file (if not a path with / found, default to results directory). if not provided, the result file will be like <template_name>.<timestamp>.result
```

# What gofetch WILL NOT DO

- Provide a persistence layer, like an ORM framework
- Be focused on standard SQL databases. Probably there is a better way to do this to relational databases.
- Be a ETL tool. Please use Luigi, Airflow or the like

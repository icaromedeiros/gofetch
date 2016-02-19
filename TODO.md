# TODO

## MVP

- Define CLI and args, write parser, define convention (e.g. directories)
- Render Jinja Hive SQL template
- Execute Hive process locally with rendered query using envoy or subprocess with a standard csv with header result
- Execute remotely
- Add a config to args (ymls?),
  * maybe with a conventioned directory to reuse configs such as db connection and fix tables (config is precedent over args)
  * Use https://github.com/henriquebastos/python-decouple ?
  * use https://github.com/rochacbruno/dynaconf ?
  * Use https://github.com/osantana/prettyconf ?
- Test with Spark SQL and other forms of queries (make the template language agnostic)
- Handle execution log files (conventioned dir)

## Enhancements

- Add quickstart tool (create directories, examples, etc)
- Add template creators (inform engine and fixed parameters)
- Create a django admin (or alike) to manage queries including metadata such as tags to ease search and encourage reuse
- Execute queries within python (i.e. without hive command), using official drivers (contrib?)
- More options to rendered result (dataframe pickle, sql, etc)
- Use some library to better render results?
   * https://github.com/turicas/rows
   * https://github.com/EliotBerriot/lifter

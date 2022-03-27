#
# Create Database Schema
#
# Input:
#   hostname        - database hostname
#   user            - database username
#   password        - database password
#   databaseName    - database schema name
#
# Output:
#   Information sent to stdout and stderr.  Exits on first error encountered.
#
function createDatabase()
{
    if [ $# != 4 ]; then
        echo "ERROR: createDatabase - invalid args: '$*' count: $#"
        exit 1
    fi

    hostname=$1
    user=$2
    password=$3
    databaseName=$4

    statement="CREATE DATABASE "
    statement+="$databaseName"
    statement+=" ENCODING = UTF8"
    statement+=";"

    export PGPASSWORD=$password
    psql -h $hostname -U $user -d postgres -w -v "ON_ERROR_STOP=1" -c "${statement}"
}

# Use Database to verify it exists
#
# Input:
#   hostname        - database hostname
#   user            - database username
#   password        - database password
#   databaseName    - database schema name
#
# Output:
#   Information sent to stdout and stderr.  Exits on first error encountered.
#
function useDatabase()
{
    if [ $# != 4 ]; then
        echo "ERROR: useDatabase - invalid args: '$*' count: $#"
        exit 1
    fi

    hostname=$1
    user=$2
    password=$3
    databaseName=$4

    statement="\c "
    statement+="$databaseName"
    statement+=";"

    export PGPASSWORD=$password
    psql -h $hostname -U $user -d postgres -w -v "ON_ERROR_STOP=1" -c "${statement}"
}

function installScript()
{
    if [ $# != 5 ]; then
        echo "ERROR: installScript - invalid args: '$*' count: $#"
        exit 1
    fi

    hostname=$1
    user=$2
    password=$3
    databaseName=$4
    files=$5

    for f in $files
    do
        # Execute file, display output and exit on error
        echo "Installing $f ..."
        export PGPASSWORD=$password
        psql -h $hostname -U $user -w -v "ON_ERROR_STOP=1" $databaseName < $f
    done
}

function displayPsqlOutputExitOnError()
{
    error=$1

    if [ $error != 0 ]; then
        echo "================================================="
        echo "==== Last 25 lines in $PSQL_OUTPUT_FILE file ===="
        echo "================================================="
        tail -25 $PSQL_OUTPUT_FILE
        exit $error
    fi
}
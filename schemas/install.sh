source ./helpers.sh

hostname=$1
user=$2
password=$3
databaseName=$4

createDatabase $hostname $user $password $databaseName
useDatabase $hostname $user $password $databaseName
installScript $hostname $user $password $databaseName "./tables/*.sql"

# export PGPASSWORD=$password
# psql -h localhost -U macbook -d postgres -w -v "ON_ERROR_STOP=1" -c "CREATE DATABASE merketfy_dev;"
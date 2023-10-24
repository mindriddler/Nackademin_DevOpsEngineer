package demo;
use Dancer ':syntax';
use DBI;
use Data::Dumper;

our $VERSION = '0.1';

our $dbi = DBI->connect(
                        config->{dbconnect},
                        config->{dbuser},
                        config->{dbpass},
                        {RaiseError => 1, PrintError => 0}
                       ) or die $DBI::errstr;

# Try to create our table, just ignore any problems (such as it already existing).
eval {
    $dbi->do(q[CREATE TABLE demodata (address varchar(255), uri varchar(255), tstamp integer)]);
};

my $store_sth = $dbi->prepare(q[INSERT INTO demodata VALUES (?,?,?)]);
my $fetch_sth = $dbi->prepare(q[SELECT address, uri, tstamp FROM demodata ORDER BY tstamp DESC LIMIT 100]);

get qr{/(.*)} => sub {
    my $client_ip = request->header('X-Forwarded-For') || request->address;
    $store_sth->execute($client_ip, request->uri, time());
    my $data = $dbi->selectall_arrayref($fetch_sth);
    for my $row (@$data) {
        # Convert time_t value to readable string
        $row->[2] = scalar(localtime($row->[2]))
    }

    template 'index', {rows => $data};
};

true;

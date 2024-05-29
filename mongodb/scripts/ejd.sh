#!/bin/bash

mongo --host localhost --port 27017 <<EOF
use music;

db.albums.aggregate(
  {\$group: {_id:"\$Artist", score: {\$sum:"\$score"}}}
);

EOF
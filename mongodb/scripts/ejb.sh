#!/bin/bash


mongo --host localhost --port 27017 <<EOF
use music;

db.albums.aggregate([
  { \$group: { _id: "\$Year", count: { \$sum: 1 } } },
  { \$sort: { count: -1 } }
]).forEach(printjson);

EOF
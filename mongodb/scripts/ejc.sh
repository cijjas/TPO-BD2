#!/bin/bash



mongo --host localhost --port 27017 <<EOF
use music;

db.albums.updateMany(
  {},
  [{ \$set: { score: { \$subtract: [501, "\$Number"] } } }]
);
EOF
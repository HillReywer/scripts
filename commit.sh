#!/bin/bash
git add .
git commit -m "$(curl -s whatthecommit.com/index.txt)"
git push
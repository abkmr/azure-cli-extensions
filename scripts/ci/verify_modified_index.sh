#!/usr/bin/env bash
set -ex

# Install CLI & Dev Tools
echo "Installing azure-cli-dev-tools and azure-cli..."
git clone --single-branch -b dev https://github.com/Azure/azure-cli.git ../azure-cli

pip install azdev
azdev setup -c ../azure-cli

echo "Installed."
az --version
set +x

# check for index updates
modified_extensions=$(python ./scripts/ci/index_changes.py)
echo "Found the following modified extension entries:"
echo "$modified_extensions"

# run linter on each modified extension entry
while read line; do
    if [ -z "$line" ]; then
        continue
    fi
    part_array=($line)
    ext=${part_array[0]}
    source=${part_array[1]}
    echo
    echo "New index entries detected for extension:" $ext
    echo "Adding latest entry from source:" $source

    az extension add -s $source -y

    # TODO migrate to public azdev
    echo "Load all commands..."
#    azdev verify load-all

    # TODO migrate to public azdev
    echo "Running linter..."
#    azdev cli-lint --ci --extensions $ext

    az extension remove -n $ext

    echo $ext "extension has been removed."
done <<< "$modified_extensions"

echo "OK. Completed Verification of Modified Extensions."

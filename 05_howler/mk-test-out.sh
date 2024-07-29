#!/usr/bin/env bash

set -U

PRG="/.howler.py"
IN_DIR="../inputs"
OUT_DIR="test-outs"

[[ ! -d "${OUT_DIR}" ]] && mkidr -p "${OUT_DIR}"

for FILE in sonnet-29.txt the-bustle.txt preamble.txt; do
    IN_FILE="${IN_DIR}/${FILE}"
    OUT_FILE="${OUT_DIR}/${FILE}"

    if [[ -f "${IN_FILE}" ]]; then
        $PRG "${IN_FILE}" -o "${OUT_FILE}"
    fi
done

echo "Done."

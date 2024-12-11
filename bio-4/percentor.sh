#!/bin/bash

GREEN='\033[0;42m'
RED='\033[0;41m'
BLUE='\033[0;44m'
NC='\033[0m'

if [ "$#" -ne 2 ]; then
    echo -e "${RED}Error: Required 2 arguments.${NC}"
    exit 1
fi

REFERENCE_GENOME="$1"
READS="$2"

echo -e "${BLUE}Running FastQC...${NC}"
fastq-dump "$READS"

echo -e "${BLUE}Indexing reference genome...${NC}"
bwa index "$REFERENCE_GENOME"

echo -e "${BLUE}Aligning reads...${NC}"
bwa mem "$REFERENCE_GENOME" "$READS" > aligned_reads.sam

echo -e "${BLUE}Running samtools flagstat...${NC}"
FLAGSTAT_LOG=$(samtools flagstat aligned_reads.sam)
echo "${FLAGSTAT_LOG}"

echo -e "${BLUE}Analyzing mapping percentage...${NC}"
PRCNTG=$(echo "$FLAGSTAT_LOG" | grep -oP 'mapped \(\K[\d.]+(?=%)')

if [ -n "$PRCNTG" ]; then
    echo -e "${GREEN}Mapped ${PRCNTG}%${NC}"
    if (( $(echo "$PRCNTG > 90.0" | bc -l ) )); then
        echo -e "${GREEN}OK${NC}"
    else
        echo -e "${RED}Not OK${NC}"
    fi
else
    echo -e "${RED}Failed to get percentage${NC}"
fi
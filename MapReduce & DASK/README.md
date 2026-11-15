# Text processing with MapReduce & Dask

A Python coursework project exploring text preparation, MongoDB updates, map/reduce aggregation, sorting and TF-IDF ranking.

## Implementation map

| File | Input | Processing / output |
| --- | --- | --- |
| [task1.py](task1.py) | Local MongoDB `Practical4.asm` | Cleans text and updates keyword, entity, topic and sentiment fields |
| [txt.py](txt.py) | Local MongoDB `Practical4.asm` | Writes prepared inputs to `task2.txt`, `task3.txt`, `task4.txt`, `task5.txt` |
| [task2.py](task2.py) | Whitespace-delimited text | Lowercase word counts using mrjob |
| [task3.py](task3.py) | One location string per line | Location counts using mrjob |
| [task4.py](task4.py) | Comma-separated ID/text records | Sorts records by integer ID in a reducer |
| [task4_2.py](task4_2.py) | `task4.txt` | In-memory merge sort; writes `result4_2.txt` |
| [task5.py](task5.py) | `task5.txt` and an interactive top-N value | Fits TF-IDF, converts a pandas frame to Dask, sorts and writes `result5.csv` |

The `result*` files are committed output artifacts. Their presence does not establish a fresh successful run.

## Getting started

Work from this project directory so relative file paths resolve correctly. For the two standalone counting scripts, install Python and `mrjob` in an isolated environment. The following commands are derived from the entry points and have not yet been validated in a clean environment:

```bash
cd "MapReduce & DASK"
python task2.py task2.txt > word-count-review.jsonl
python task3.py task3.txt > city-count-review.jsonl
```

The preprocessing scripts additionally import `pymongo`, `nltk`, `gensim` and `rake_nltk`. They require a local MongoDB service, a populated `Practical4.asm` collection and the appropriate NLTK resources. The MongoDB seed data and a tested environment specification are not supplied.

`task1.py` writes to MongoDB using `actor.id` as the update filter. Review that matching behavior on a disposable copy before running it: multiple records may share an actor.

## Engineering boundaries

- TF-IDF is fitted in memory before conversion to Dask. This is not distributed TF-IDF training or evidence of a cluster deployment.
- `task4.py` collects records under a single reducer key; sorting can become a memory bottleneck.
- Its printed timer is calculated before `Sort_ID.run()` and should not be used as a job benchmark.
- Input paths and MongoDB settings are hard-coded; automated tests, retries and scheduling are not implemented.
- The stopword removal functions mutate a list while iterating; add a regression fixture before changing this logic.

## Next improvements

1. Add synthetic inputs and exact-output tests for word and city counts.
2. Capture a tested environment and document the input schema.
3. Replace hard-coded configuration with explicit arguments.
4. Measure actual execution and report input/output counts and failures.

[Back to portfolio](../README.md)

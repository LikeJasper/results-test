# Results test

## Requirements

You need python3 and scipy installed.

## Usage

### 1. Basic usage with default success rate of >90% and desired confidence level of ≥95%:
```
python3 test.py [no. successes] [no. trials]
```
E.g. with 85 successes out of 92 trials:
```
python3 test.py 85 92
```
### 2. Usage with specified success rate:
```
python3 test.py [no. successes] [no. trials] [target successes percentage]
```
E.g. with 85 successes out of 92 trials, where a success rate of 80% is desired:
```
python3 test.py 85 92 80
```
### 3. Usage with specified success rate and specified confidence level:
```
python3 test.py [no. successes] [no. trials] [target successes percentage] [target confidence level]
```
E.g. with 85 successes out of 92 trials, where a success rate of 80% and a confidence level of 99% is desired:
```
python3 test.py 85 92 80 99
```

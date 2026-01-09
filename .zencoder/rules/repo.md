---
description: Repository Information Overview
alwaysApply: true
---

# GitHub Activity Generator Information

## Summary
GitHub Activity Generator is a Python script that helps users instantly generate a beautiful GitHub contributions graph for the last year. The script creates a local git repository with backdated commits distributed across specified time periods, then pushes to a remote repository. It's designed for educational purposes to demonstrate GitHub mechanics and includes customizable commit frequency, maximum commits per day, and date range options.

## Structure
- **contribute.py**: Main entry point script that generates commits with backdated timestamps
- **test_contribute.py**: Unit tests for the contribution generation logic
- **.github/workflows/build.yml**: CI/CD pipeline configuration for automated testing
- **LICENSE**: Project license file
- **.github/README.md**: Primary project documentation

## Language & Runtime
**Language**: Python  
**Versions Tested**: Python 3.8, 3.9, 3.10, 3.11  
**Build System**: Standard Python execution  
**Package Manager**: pip

## Dependencies
**Runtime Dependencies**: None specified (uses only Python standard library)

**Development Dependencies**:
- flake8 (for code linting)

## Build & Installation

### System Requirements
- Python (3.8 or later)
- Git

### Execution
```bash
python contribute.py --repository=git@github.com:user/repo.git
```

### Custom Options
```bash
python contribute.py --max_commits=12 --frequency=60 --no_weekends --days_before=10 --days_after=15
```

## Testing

**Framework**: unittest (Python standard library)  
**Test Location**: test_contribute.py  
**Naming Convention**: Test methods prefixed with `test_`  
**Configuration**: Native unittest configuration

**Run Command**:
```bash
python -m unittest test_contribute
```

## CI/CD

**Workflow**: GitHub Actions (.github/workflows/build.yml)  
**Trigger**: On push and pull request  
**Test Matrix**: Python 3.8, 3.9, 3.10, 3.11  
**Quality Checks**:
- Lint with flake8 on both contribute.py and test_contribute.py
- Unit tests execution across all Python versions

## Key Command-Line Arguments

- `-r, --repository`: Remote git repository URL (SSH or HTTPS)
- `-mc, --max_commits`: Maximum commits per day (1-20, default: 10)
- `-fr, --frequency`: Percentage of days to commit on (default: 80%)
- `-nw, --no_weekends`: Skip weekends when generating commits
- `-db, --days_before`: Days before current date to start committing (default: 365)
- `-da, --days_after`: Days after current date to continue committing (default: 0)
- `-un, --user_name`: Override local git user.name config
- `-ue, --user_email`: Override local git user.email config

# About
This code is similar to a "one time pad" (aka Vernam Cipher) which can be used to encode/decode messages.

# Notes
- The key must be the same length as the uncoded text.
- The key must be truly random.
- The key must never be reused, in whole or in part.
- The key must be kept completely secret by the communicating parties.
- Consider adding (or using) a character (or phrase) that indicates that the message was sent under duress.

# Development
For development, run the following commands.

## create python environment
    python3 -m venv venv
    source venv/bin/activate
    pip install pytest pytest-cov

## run the unit tests
    make test

## show code coverage
    make cov

## building for distribution
    python3 -m pip install --upgrade build
    python3 -m build
    python3 -m pip install --upgrade twine

## distribute to pypi
    make release

#!/bin/bash
cd /home/kavia/workspace/code-generation/prime-commerce-platform-138358-138367/amazon_clone_backend
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi


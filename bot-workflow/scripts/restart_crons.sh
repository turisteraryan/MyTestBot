#!/bin/bash

# Check if the cron job is running
if ! crontab -l | grep -q "auto_restart.py"; then
    echo "Setting up cron job to restart workflow..."
    (crontab -l; echo "0 */6 * * * /usr/bin/python /path/to/bot-workflow/scripts/auto_restart.py") | crontab -
    echo "Cron job added."
else
    echo "Cron job is already running."
fi


#!/usr/bin/env python
import subprocess
import click
import re

@click.command()
@click.option('--mode')
@click.option('--value', default=5)
def main(mode, value):

    if (mode == '+'):
        command = 'pactl get-sink-volume 0'
        output = subprocess.run(command, stdout=subprocess.PIPE, shell=True).stdout
        volume = int(re.sub(r'[^\d]', '', str(output.split()[4])))
        
        if volume + value >= 100:
            value = 100 - volume
        
    command = f'pactl set-sink-volume 0 {mode}{value}%'
    subprocess.run(command, shell=True)

if __name__ == '__main__':
    main()

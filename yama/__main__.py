from core import YAMA
import click


def save_to(save_to_file, content):
    with open(save_to_file, 'w') as outfile:
        outfile.write(content)


@click.command()
@click.option(
    '--yama-input-file', '-i',
    type=click.Path(exists=True),
    help='YAMA Input File',
    prompt=True, required=True,
)
@click.option(
    '--template-file', '-t',
    type=click.Path(exists=True),
    help='Template File',
    prompt=True, required=True,
)
@click.option(
    '--output', '-o',
    type=click.Path(),
    help='Save output to file',
)
def main(yama_input_file, template_file, output):
    ap = YAMA(yama_input_file)
    rendered_output = ap.render(template_file)
    if output:
        save_to(output, rendered_output)
    else:
        click.echo(rendered_output)


if __name__ == '__main__':
    main()

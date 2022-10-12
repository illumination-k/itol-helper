import argparse

from itolhelper import handlers
from itolhelper.pretty_logger import set_loglevel, set_loglevel_args


def main():
    parser = argparse.ArgumentParser()
    parser = set_loglevel_args(parser)

    subparsers = parser.add_subparsers()

    upload_parser = subparsers.add_parser("upload")
    upload_parser.add_argument(
        "--api-key",
        type=str,
        default=None,
        help="Using ITOL_APIKEY environment variable for default",
    )

    upload_parser.add_argument("-p", "--project-name", type=str, required=True)
    upload_parser.add_argument("--tree-name", type=str, default=None)
    upload_parser.add_argument("--tree-description", type=str, default=None)
    upload_parser.add_argument("-d", "--dir", type=str, required=True)
    upload_parser.set_defaults(handler=handlers.upload)

    text_parser = subparsers.add_parser("text")
    text_parser.add_argument("-i", "--ids", type=str, required=True, help="contains id file")
    text_parser.add_argument("-c", "--config", type=str, required=True, help="config file")
    text_parser.add_argument("-l", "--label", type=str, default="text")
    text_parser.set_defaults(handler=handlers.text)
    
    style_parser = subparsers.add_parser("style")
    style_parser.add_argument("-i", "--ids", type=str, required=True, help="contains id file")
    style_parser.add_argument("-c", "--config", type=str, required=True, help="config file")
    style_parser.add_argument("-l", "--label", type=str, default="style")
    style_parser.set_defaults(handler=handlers.style)

    args = parser.parse_args()

    set_loglevel(args.loglevel)

    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

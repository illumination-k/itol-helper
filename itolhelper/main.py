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
    text_parser.add_argument(
        "-i", "--ids", type=str, required=True, help="file contained ID (nwk, fasta, phy or txt)"
    )
    text_parser.add_argument("-c", "--config", type=str, required=True, help="config file")
    text_parser.add_argument("-l", "--label", type=str, default="aliases")
    text_parser.set_defaults(handler=handlers.text)

    style_parser = subparsers.add_parser("style")
    style_parser.add_argument(
        "-i", "--ids", type=str, required=True, help="file contained ID (nwk, fasta, phy or txt)"
    )
    style_parser.add_argument("-c", "--config", type=str, required=True, help="config file")
    style_parser.add_argument("-l", "--label", type=str, default="label-style")
    style_parser.set_defaults(handler=handlers.style)

    alignment_parser = subparsers.add_parser("alignment")
    alignment_parser.add_argument(
        "-i",
        "--input",
        type=str,
        required=True,
        help="file contained multple alignment. fasta and phy are supported",
    )
    alignment_parser.add_argument("-l", "--label", type=str, default="alignment")
    alignment_parser.set_defaults(handler=handlers.alignment)

    branch_symbol_parser = subparsers.add_parser("branch-symbols")
    branch_symbol_parser.add_argument(
        "-i", "--ids", type=str, required=True, help="file contained ID (nwk, fasta, phy or txt)"
    )
    branch_symbol_parser.add_argument("-c", "--config", type=str, required=True, help="config file")
    branch_symbol_parser.add_argument("-l", "--label", type=str, default="branch-symbols")
    branch_symbol_parser.set_defaults(handler=handlers.branch_symbols)

    args = parser.parse_args()

    set_loglevel(args.loglevel)

    if hasattr(args, "handler"):
        args.handler(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

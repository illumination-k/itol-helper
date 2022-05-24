import argparse

from handlers.upload import UploadParams


def main():
    print(UploadParams(api_key="aaa", project_name="bbb").dict(exclude_none=True))


if __name__ == "__main__":
    main()

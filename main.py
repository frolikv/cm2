import argparse

class CLI:
    def __init__(self):
        self.params = self.cmd_line()
        self.print_args()


    def cmd_line(self):
        params = {}
        parser = argparse.ArgumentParser(description="CLI")

        parser.add_argument('--package-name', '-p',
                            type=str,
                            required=True,
                            help="package name"
                            )

        parser.add_argument('--url', '-u',
                            type=str,
                            required=True,
                            help="url address or file path"
                            )

        parser.add_argument('--mode', '-m',
                            type=str,
                            default='r',
                            help="work mode"
                            )

        parser.add_argument('--file-name', '-n',
                            type=str,
                            default='graph.png',
                            help="generated file name"
                            )

        parser.add_argument('--max-depth', '-d',
                            type=int,
                            default=5,
                            help="name of graph file"
                            )

        parser.add_argument('--filter', '-f',
                            type=str,
                            default='',
                            help="name of graph file"
                            )

        args = parser.parse_args()
        # print(args)

        params['package_name'] = args.package_name
        params['url'] = args.url
        params['mode'] = args.mode
        params['file_name'] = args.file_name
        params['max_depth'] = args.max_depth
        params['filter'] = args.filter
        return params

    def print_args(self):
        print(f"package-name:\t{self.params['package_name']}")
        print(f"url:\t\t{self.params['url']}")
        print(f"mode:\t\t{self.params['mode']}")
        print(f"file_name:\t{self.params['file_name']}")
        print(f"max_depth:\t{self.params['max_depth']}")
        print(f"filter:\t\t{self.params['filter']}")


cli = CLI()
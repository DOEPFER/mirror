# Mirror

Mirror creates an exact copy of the directory specified in `--source` to the directory specified in `--mirror`.

> **Warning**
> The file synchronization flow is strictly one-way: `--source` -> `--mirror`.
> Any content (files and folders) in the `--mirror` directory that is not present in the `--source` directory will be permanently deleted to maintain an exact replica of the source. Swapping the directories in the `--source` and `--mirror` arguments may result in severe file loss.

## Usage

You can run the script from the command line. Here are some examples based on the available arguments:

### Basic Synchronization

```bash
python mirror.py --source /path/to/source_dir --mirror /path/to/mirror_dir
```

### Advanced Usage (with ignore list, custom log prefix, and verbose mode)

```bash
python mirror.py -s /path/to/source_dir -m /path/to/mirror_dir -i .git node_modules __pycache__ -l my_sync_log -v
```

### Available Arguments
| Argument | Short | Description | Default |
|---|---|---|---|
| `--source` | `-s` | Source directory. | |
| `--mirror` | `-m` | Mirror directory. | |
| `--ignore` | `-i` | Directories to ignore. Search scope: recursive. (Accepts multiple items) | |
| `--logprefix`| `-l` | Log file prefix. | `mirror` |
| `--verbose` | `-v` | Verbose mode. | `False` |
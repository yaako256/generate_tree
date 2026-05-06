# generate_tree.py
import sys
from pathlib import Path

# ツリー描画用の記号
SPACE =  '    '
BRANCH = '├── '
LAST_BRANCH = '└── '
VERTICAL = '│   '

def count_items_recursive(directory, max_depth, current_depth=1):
    """指定された深さまで全アイテムを再帰的にカウント"""
    if current_depth > max_depth:
        return 0
    try:
        count = 0
        for p in directory.iterdir():
            count += 1
            if p.is_dir():
                count += count_items_recursive(p, max_depth, current_depth + 1)
        return count
    except PermissionError:
        return 0

def draw_tree(directory, max_depth, current_depth=1, prefix=""):
    """指定された深さまでツリーを描画"""
    if current_depth > max_depth:
        return

    try:
        all_paths = list(directory.iterdir())
    except PermissionError:
        return

    # 1. ファイルとディレクトリを分ける
    files = sorted([p for p in all_paths if p.is_file()], key=lambda p: p.name.lower())
    
    # 2. ディレクトリを「制限された深さまでの合計数」でソート
    dirs_with_counts = []
    for d in [p for p in all_paths if p.is_dir()]:
        # カウント時も現在の深さを考慮して、残り何階層分見るかを計算
        c = count_items_recursive(d, max_depth, current_depth + 1)
        dirs_with_counts.append((d, c))
    
    dirs_with_counts.sort(key=lambda x: (x[1], x[0].name.lower()))
    dirs = [d[0] for d in dirs_with_counts]
    
    paths = files + dirs
    count = len(paths)

    for i, path in enumerate(paths):
        is_last = (i == count - 1)
        connector = LAST_BRANCH if is_last else BRANCH
        suffix = "/" if path.is_dir() else ""
        
        print(f"{prefix}{connector}{path.name}{suffix}")
        
        if path.is_dir():
            new_prefix = prefix + (SPACE if is_last else VERTICAL)
            draw_tree(path, max_depth, current_depth + 1, new_prefix)

def main():
    # 引数の解析
    # python tree.py [path] [depth]
    target_path = Path('.')
    max_depth = float('inf') # デフォルトは無制限

    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])
    
    if len(sys.argv) > 2:
        try:
            max_depth = int(sys.argv[2])
        except ValueError:
            print("Error: 深さは数値で指定してください。")
            return

    if not target_path.exists():
        print(f"Error: {target_path} は存在しません。")
        return

    print(f"{target_path.resolve().name}/")
    draw_tree(target_path, max_depth)

if __name__ == "__main__":
    main()
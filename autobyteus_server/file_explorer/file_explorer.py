# autobyteus_server/file_explorer/file_explorer.py

from autobyteus_server.file_explorer.tree_node import TreeNode
from autobyteus_server.file_explorer.directory_traversal import DirectoryTraversal
from autobyteus_server.file_explorer.traversal_ignore_strategy.dot_ignore_strategy import DotIgnoreStrategy
from autobyteus_server.file_explorer.traversal_ignore_strategy.git_ignore_strategy import GitIgnoreStrategy
from autobyteus_server.file_explorer.traversal_ignore_strategy.specific_folder_ignore_strategy import SpecificFolderIgnoreStrategy

class FileExplorer:
    """
    Class to manage workspace directory tree.
    """
    def __init__(self, workspace_root_path: str = None):
        """
        Initialize FileExplorer.
        """
        self.root_node = None
        self.workspace_root_path = workspace_root_path

    def build_workspace_directory_tree(self) -> TreeNode:
        """
        Builds and returns the directory tree of a workspace.

        Returns:
            TreeNode: The root TreeNode of the directory tree.
        """
        if not self.workspace_root_path:
            raise ValueError("Workspace root path is not set")

        files_ignore_strategies = [
            SpecificFolderIgnoreStrategy(folders_to_ignore=['.git']),
            GitIgnoreStrategy(root_path=self.workspace_root_path),
            DotIgnoreStrategy()
        ]
        directory_traversal = DirectoryTraversal(strategies=files_ignore_strategies)

        self.root_node = directory_traversal.build_tree(self.workspace_root_path)
        return self.root_node

    def add_file_or_folder(self, file_or_folder_path: str):
        """
        Adds a file or folder to the workspace directory tree.
        Args:
            file_or_folder_path (str): The path of the file or folder to be added.
        """
        # Code to add the file or folder to the tree

    def remove_file_or_folder(self, file_or_folder_path: str):
        """
        Removes a file or folder from the workspace directory tree.
        Args:
            file_or_folder_path (str): The path of the file or folder to be removed.
        """
        # Code to remove the file or folder from the tree

    def get_tree(self) -> TreeNode:
        """
        Gets the workspace directory tree.
        Returns:
            TreeNode: The root node of the workspace directory tree.
        """
        return self.root_node

    def to_json(self):
        """
        Returns a JSON representation of the workspace directory tree.
        Returns:
            JSON: The JSON representation of the workspace directory tree.
        """
        return self.root_node.to_json()
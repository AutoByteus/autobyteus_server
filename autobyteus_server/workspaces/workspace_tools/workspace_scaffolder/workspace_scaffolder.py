"""
Workspace Scaffolder Module.

This module provides the scaffolding logic for workspaces based on the type of project.
It determines the type of project and then applies the respective project scaffolder.
"""

from autobyteus_server.workspaces.workspace import Workspace
from autobyteus_server.workspaces.workspace_tools.base_workspace_tool import BaseWorkspaceTool
from autobyteus_server.workspaces.workspace_tools.workspace_scaffolder.python_project_scaffolder import PythonProjectScaffolder
from autobyteus_server.workspaces.workspace_tools.workspace_scaffolder.react_project_scaffolder import ReactProjectScaffolder
from autobyteus_server.workspaces.workspace_tools.workspace_scaffolder.java_project_scaffolder import JavaProjectScaffolder

class WorkspaceScaffolder(BaseWorkspaceTool):
    """
    Workspace Scaffolder class to set up default project structures 
    depending on the project type.
    """

    def __init__(self, workspace: Workspace):
        """
        Constructor for WorkspaceScaffolder.

        Args:
            workspace (Workspace): The workspace to be scaffolded.
        """
        super().__init__(workspace)

        if self.workspace.project_type == "python":
            self.project_scaffolder = PythonProjectScaffolder(workspace)
        elif self.workspace.project_type == "react":
            self.project_scaffolder = ReactProjectScaffolder(workspace)
        elif self.workspace.project_type == "java":
            self.project_scaffolder = JavaProjectScaffolder(workspace)
        else:
            raise ValueError(f"Unsupported project type: {self.workspace.project_type}")

    def execute(self):
        """
        Execute the scaffolding process on the workspace.
        """
        self.project_scaffolder.scaffold()
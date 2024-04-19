private import python
private import semmle.python.dataflow.new.DataFlow
private import semmle.python.Concepts
private import semmle.python.ApiGraphs

private module Shell {
    API::Node invoke() {
        result = API::moduleImport("shell").getMember("shell")
    }

    private class ShellRunCommandCall extends SystemCommandExecution::Range, DataFlow::CallCfgNode {
        ShellRunCommandCall() {
            this = invoke().getACall()
        }

        override DataFlow::Node getCommand() {
            result in [this.getArg(0), this.getArgByName("command")]
        }
    }
}
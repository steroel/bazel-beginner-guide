load("//:my_custom_rule.bzl", "write_new_file", "write_new_file_with_custom_tool")

load("@rules_python//python:defs.bzl", "py_binary")

py_binary(
  name = "my_build_tool",
  srcs = ["my_build_tool.py"],
)

write_new_file_with_custom_tool(
    name = "build_with_custom_tool",
    my_input_file = "//:my_input_file.txt",
    output_file_name = "my_output_file_with_custom_tool",
    my_custom_build_tool = ":my_build_tool"
)

write_new_file(
    name = "write_my_custom_message_info_file",
    my_input_file = "//:my_input_file.txt",
    output_file_name = "my_output_file",
)

write_new_file(
    name = "write_something_else",
    my_input_file = "//:my_input_file.txt",
    output_file_name = "my_something_else",
)


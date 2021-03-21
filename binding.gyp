{
  "targets": [
    {
      "target_name": "addon",
      # this does not work
      # "sources": ["src/*"]
      # this does
      "sources": [
        "src/addon.cc",
        "src/myobject.cc"
      ]
    }
  ]
}
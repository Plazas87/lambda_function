module.exports = {
    extends: ["@commitlint/config-conventional"],
    rules: {
        "type-enum": [
            2,
            "always",
            [
                "assets",
                "build",
                "chore",
                "ci",
                "config",
                "docs",
                "downgrade",
                "feat",
                "fix",
                "format",
                "hotfix",
                "initial",
                "locales",
                "merge",
                "perf",
                "refactor",
                "remove",
                "rename",
                "revert",
                "review",
                "security",
                "seo",
                "style",
                "test",
                "upgrade",
                "ux",
                "wip",
            ],
        ],
        "scope-enum": [
            2,
            "always",
            [
                "galeo_lambda",
            ],
        ],
    },
};

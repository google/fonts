# Only run gftools qa on prs which contain font files.

PR_FILES=https://api.github.com/repos/$TRAVIS_REPO_SLUG/pulls/$TRAVIS_PULL_REQUEST/files
HAS_FONTS=$(curl -H "Authorization: token $GH_TOKEN" $PR_FILES | jq '[.[] | .filename | test("ttf|otf")] | any')

if [ "$HAS_FONTS" = true ];
then
    echo "Running gftools qa"
    gftools qa -pr https://github.com/$TRAVIS_REPO_SLUG/pulls/$TRAVIS_PULL_REQUEST -gfb -a -o qa -ogh
else
    echo "Skipping. No fonts in PR"
fi

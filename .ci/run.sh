# Only run gftools qa on prs which have modified files in directories which
# contain font binaries.

# Find directories which contain files that have been altered or added. Also
# Skip /static directories.
CHANGED_DIRS=$(git diff origin/main --dirstat=files --diff-filter d | sed "s/[0-9. ].*%//g" | grep -v "static")
OUT=out

PR_URL="$GITHUB_SERVER_URL/$GITHUB_REPOSITORY/pull/$PR_NUMBER"
echo "PR url: $PR_URL"

for dir in $CHANGED_DIRS
do
    font_count=$(ls -1 $dir*.ttf 2>/dev/null | wc -l)
    is_designer_dir=$(echo $dir | grep "designers")
    if [ $font_count != 0 ]
    then
	echo "Checking $dir"
	mkdir -p $OUT
	# If pr contains modified fonts, check with Fontbakery, Diffenator and DiffBrowsers.
	# If pr doesn't contain modified fonts, just check with Fontbakery.
	modified_fonts=$(git diff --name-only origin/main HEAD $dir*.ttf)
	if [ -n "$modified_fonts" ]
	then
	    echo "Fonts have been modified. Checking fonts with all tools"
	    gftools qa -f $dir*.ttf -gfb -a -o $OUT/$(basename $dir)_qa --out-url $PR_URL
	else
	    echo "Fonts have not been modified. Checking fonts with Fontbakery only"
	    gftools qa -f $dir*.ttf --fontbakery -o $OUT/$(basename $dir)_qa --out-url $PR_URL
	fi
    elif [ ! -z $is_designer_dir ]
    then
        echo "Checking designer profile"
        pytest .ci/test_profiles.py $dir
    else
	echo "Skipping $dir. Directory does not contain fonts"
    fi
done


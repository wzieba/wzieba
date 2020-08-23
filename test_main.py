from unittest import TestCase

from main import replace_content, BlogEntry, fetch_and_parse_rss_feed

EXPECTED_CONTENT = "This is expected content in target block"

EXPECTED_RESULT = """#Header

<!-- blog starts -->
""" + EXPECTED_CONTENT + """
<!-- blog ends -->

And some content **not** to replace."""


class Test(TestCase):
    def test_replace_content_for_block(self):
        # given
        test_readme_file = open("testREADME.md", "r")

        # when
        replaced_content = replace_content(
            content=test_readme_file.read(),
            block_marker="blog",
            new_content=EXPECTED_CONTENT
        )

        # then
        self.assertEqual(
            EXPECTED_RESULT,
            replaced_content
        )

        test_readme_file.close()

    def test_parse_xml_rss(self):
        # given
        expected_entries = [
            BlogEntry(
                title='Github Actions + Fastlane + Firebase App Distribution (or App Center)',
                url='https://medium.com/@wzieba/github-actions-fastlane-firebase-app-distribution-or-app-center'
                    '-4fadbdff63f9?source=rss-117db94a0177------2',
                published='2-8-2020'
            ),
            BlogEntry(
                title='String escape sequences while reading String from a file in Kotlin/Java',
                url='https://medium.com/@wzieba/string-escape-sequences-while-reading-string-from-a-file-in-kotlin'
                    '-java-77b4249e5330?source=rss-117db94a0177------2',
                published='26-7-2020'
            ),
            BlogEntry(
                title='Count change algorithm.',
                url='https://medium.com/@wzieba/count-change-algorithm-df8864f68e76?source=rss-117db94a0177------2',
                published='27-1-2017'
            )
        ]

        # when
        parsed = fetch_and_parse_rss_feed('@wzieba')

        # then
        self.assertEqual(parsed, expected_entries)

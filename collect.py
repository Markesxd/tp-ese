from random import randint
from time import sleep
from pydriller import Repository
from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
from textblob.sentiments import NaiveBayesAnalyzer
from datetime import datetime
from threading import Thread

def wrfl(commit):
    file = open('dados.txt', '+a')
    blob = TextBlob(commit.msg, analyzer=NaiveBayesAnalyzer())
    file.write(f'> {commit.msg}\n{cl.classify(commit.msg)}\n{blob.sentiment}\n')
    file.close()


train = [
        ('Add binary search tree.', 'add'),
        ('Add big O info', 'add'),
        ('Add Trie.', 'add'),
        ('Fix README.', 'fix'),
        ('Integrate codecov.','add'),
        ('Fix binary tree node.', 'fix'),
        ('Add AVL Tree.', 'add'),
        ('Add playground.', 'add'),
        ('Add big O sheet for sorting algorithms.', 'add'),
        ('Add selection sort.', 'add'),
        ('Typos fixed (lines 81, 130, 166, 248)', 'none'),
        ('Restructure the Big O Notation table.','none'),
        ('Some text fixes.', 'fix'),
        ('Update README.md', 'none'),
        ('Fixing typos in Linked List README.es-ES.md', 'none'),
        ('Update breadthFirstSearch.js', 'none'),
        ('Update README.pl-PL.md', 'none'),
        ('fixed spelling error for hash-table', 'fix'),
        ('fix typos', 'none'),
        ('Correct inaccurate Chinese translation.', 'fix'),
        ('Correction', 'fix'),
        ('Fixes lint issues and updates npm packages', 'fix'),
        ('Adding one more exception for', 'add'),
        ('Removing unused import ', 'none'),
        ('Avoid checking for non W3C twice', 'fix'),
        ('fix bug in default durations', 'fix'),
        ('feat: Added virtual authenticator', 'add'),
        ('fix: code review changes', 'fix'),
        ('Updating testing library deps', 'none'),
        ('allow specifying which button gets clicked in pointer action class','add'),
        ('Reverting pretty-ms upgrade ', 'none'),
        ('Lots of changes: * changes the XML report format to match JUnit/Ant\'s. * improves file path handling. * allows the user to disable RTTI using the GTEST_HAS_RTTI macro. * makes the code compile with -Wswitch-enum. Trivial source code format tweak. Indents preprocessor directives. Make Google Test build cleanly on Visual Studio 2010, 2012, 2013. Also improve an error message in gtest_test_utils.py. Clang-on-Windows can support GTEST_ATTRIBUTE_UNUSED_. Noop changes to suppress compile-time warnings in WINDOWS code paths. remove unused valgrind probe Fix typo in AdvancedGuide.md Merge pull request #671 from mehagar/patch-1', 'none'), 
        ('Fix typo in AdvancedGuide.md', 'none'),
        ('Addressing comments', 'none'),
        ('Fix problem installing gtest when gmock enabled', 'fix'),
        ('Fix a bug deciding whether to enable the option to install Google Test caused by one of the dependent option dependencies not being defined yet.', 'fix'),
        ('Fixes #1198; impossible to install Google Test if Google Mock is built.', 'fix'),
        (f'Merge branch \'master\' into methodname-in-exception', 'none'),
        ('Remove gtest VS2005 projects', 'none'),
        (f'Merge branch \'master\' into fix_death_test_child_mingw_wer_issue1116', 'none'),
        ('use GTEST_ATTRIBUTE_UNUSED_ instead of dummy function', 'none'),
        ('Merge pull request #1300 from gennadiycivil/master', 'none'),
        ('Workaround for Travis issue https://goo.gl/d5eV8o', 'fix'),
        ('Wrong LICENSE file, sorry.  Corrected. [skip ci]', 'none'),
        ('moving JoinAsTuple to internal', 'none'),
        ('Fix scoped enum not working in gmock-gen.py', 'fix'),
        ('Use `$<INSTALL_PREFIX>` in `target_include_directories`', 'none'),
        ('Fix Python3 support', 'fix'),
        ('Googletest export', 'none'),
        ('Fix bazel issue', 'fix'),
        ('PiperOrigin-RevId: 223829127', 'none'),
        ('fix:  correct JSON syntax', 'fix'),
        ('Fix -Wsign-conversion error by adding static_cast', 'fix'),
        ('Update CONTRIBUTING.md', 'none'),
        ('Clarify googler PR policy', 'none'),
        ('Documentation sync working on the documentation being included with the code', 'add'),
        ('Renaming doc files to make the file names more palatable and in preparation for including documentation in sync process', 'none'),
        ('missed the actual file in previous commit', 'none'),
        ('Fix bad advice in cook book (#2308)', 'fix'),
        ('rename and apply snake_case on Documentation.md', 'none'),
        ('Fix gmock_gen to use MOCK_METHOD instead of old style macros.  Fix several related bugs in argument parsing and return types.', 'fix'),
        ('Internal change', 'none'),
        ('Revision of recent DoubleNearPredFormat change to support more toolchains.', 'add'),
        ('isnan() is a macro in C99, and std::isnan() is a function in C++11.  The previous change used `isnan` directly, and broke some tests in open source.', 'none'),
        ('Disable -Wmismatched-tags warning for struct/class tuple_size', 'none'),
        ('Remove the subprocess fallback code for older versions of Python', 'none'),
        ('Heaps more integrations tests for "click" behaviour.', 'none'),
        ('r202 Can now adjust the playback speed while the tests are running, including resuming at walk/run after stepping. Use css to improve TestRunner L&F.', 'none'),
        ('r211 whoops - forgot the license', 'none'),
        ('r238 TestRunner cached test results are now displayed correctly in Safari. Licence file for selenium-logging.js', 'fix'),
        ('r917 Recognise simple XPath expressions using regexps, and handle them using DOM-traversal, which is usually faster (SEL-81).', 'add'),
        ('r1002 Changed locator-strategy prefix to "=" (was ":") This addresses SEL-108', 'none'),
        ('r1053 Committed doco for select option by id.', 'none'),
        ('r1113 updated', 'none'),
        ('r1490 Deleting perl directory, in preparation to move perl-cpan on top of it', 'none'),
        ('r3505 Dangling _test_pageBot object after IDE closes causes showElement() to fail. Create a new object each time for now. To reproduce issue: Start IDE, attempt to [Find] using bad locator, close IDE, start IDE again, attempt to [Find] again using bad locator. You will notice the second time around, the error message is different: \'TypeError: locator.startsWith is not a function\' .', 'none'),
        ('r4545 SRC-392, SRC-389.  Fix ensureCleanSession on Safari.', 'fix'),
        ('r4586 SimonStewart: Addressing some concerns with the way that Firefox starts on Windows. In particular, when starting with a profile that needs to be tidied, such as after updating to the most recent version, there should be fewer issues', 'none'),
        ('r5147 Fixed sidebar look & feel on Mac', 'fix'),
        ('r5248 Groovy format support for *AndWait commands.', 'add'),
        ('r5694 SimonStewart: Adding the missing file.', 'fix'),
        ('r6767 EranMes: A missing underscore caused hasMatchingOverride not to be called properly. The test still passed as Firefox, does not accept a bad certificate unless explicitly allowed to and an error in this function meant it just rejected the certificate.', 'fix'),
        ('r7744 JariBakken: Moving the Proxy class out of the Remote namespace + minor style changes.', 'none'),
        ('r10207 AdamGoucher - predefining a variable to get rid of a warning', 'none'),
        ('r10234 DouniaBerrada: Renaming main android activity', 'none'),
        ('r10342 SamitBadle: Added experimental features option, made format changing experimental, refactored developer tools code and improved some code that affects issue 1244 and issue 1164 along with a bunch of small improvements. Phew!', 'add'),
        ('r12247 EranMes and AndreasHaas: Synthetic implementation of double click. Note that several functions, most notably isSelected, moved to bot.dom namespace.', 'add'),
        ('r13559 ranMes: Unify behaviour between the synthetic mouse and native mouse. Drag-and-drop tests using synthesized events now pass on all platforms and configurations (including headless X). This change should also solve incorrect MoveTargetOutOfBounds exceptions. Issue 2700 is not fixed yet, pending another change.', 'fix'),
        ('r14659 SimonStewart: Getting the selenium-backed webdriver tests passing in firefox chrome mode again', 'fix'),
        ('r15085 JimEvans: Updating .NET bindings assembly versions to 2.18.0 for impending release.', 'none'),
        ('r15616 KristianRosenvold: More buffer flushing', 'none'),
        ('r16002 KristianRosenvold: Added reset of response stream upon grid error', 'fix'),
        (f'r16155 AlexeiBarantsev: Fixing RC tests. Separating baseUrl from serverUrl, it\'s another step to be able to run RC tests on CI server.', 'fix'),
        ('During running the tests, two files are generated I believe they should be added to .gitignore, so they are not committed by mistake. Unignoring a green test bumping to 2.48.1 Java: Deleting SafariTestBase, if safari tests need a special environment it should be provided with additional rules. rb - spec updates for latest Microsoft Edge support Mention the need for a driver and how to get one in python documentation', 'none'),
        ('Fixes #2931 Separating grid internal test job from e2e tests [java] Extracting base class for driver options classes to hold type-safe setters for capabilities specified in W3C WebDriver Updating .NET Bazel build rules for NuGet dependency versions [java] Adding more unit tests to bazel build Make the prefixed routes more robust This allows redirects to be set properly. *phew* [java] Deleting unused private constructor Provide our own APIs for tracing [rb] update default cookie setting behavior with thorough documentation in specs [grid] Remove unused imports Add a `toJson` method to `Browser` so it becomes easier to use in Capabilities `python`: test function names tidy up inline with pep8  (#10490)  * `python`: apply pep8 compliant snake case to tests * fix fallout from commented test changes; update everything inside `py/test/` Co-authored-by: David Burns <david.burns@theautomatedtester.co.uk>', 'fix'),
        (' Bumping Java to 4.2.1 and updating CHANGELOG', 'none'),
]

cl = NaiveBayesClassifier(train)

# i = 0
# for commit in Repository('https://github.com/trekhleb/javascript-algorithms.git').traverse_commits():
#     p = Thread(target=wrfl, args=(commit,))
#     p.start()
#     if i % 10 == 0:
#         sleep(1)

time = datetime.now()
file = open(f'./data/dados_{time}.csv', '+a')
file.write(f'classify,sentiment_class,p_pos,p_neg\n')

for commit in Repository('https://github.com/trekhleb/javascript-algorithms.git').traverse_commits():
    blob = TextBlob(commit.msg, analyzer=NaiveBayesAnalyzer())
    file.write(f'{cl.classify(commit.msg)},{blob.sentiment[0]},{blob.sentiment[1]},{blob.sentiment[2]}\n')

print('First repository drilled successfully')

for commit in Repository('https://github.com/google/googletest.git').traverse_commits():
    blob = TextBlob(commit.msg, analyzer=NaiveBayesAnalyzer())
    file.write(f'{cl.classify(commit.msg)},{blob.sentiment[0]},{blob.sentiment[1]},{blob.sentiment[2]}\n')

print('Second repository drilled successfully')

# for commit in Repository('https://github.com/SeleniumHQ/selenium').traverse_commits():
#     blob = TextBlob(commit.msg, analyzer=NaiveBayesAnalyzer())
#     file.write(f'{cl.classify(commit.msg)},{blob.sentiment[0]},{blob.sentiment[1]},{blob.sentiment[2]}\n')

# print('Third repository drilled successfully')

file.close()
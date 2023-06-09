import unittest
from dataset_reader import DatasetReader

class TestDatasetReader(unittest.TestCase):
    def setUp(self):
        self.dataset_reader = DatasetReader()

    def test_get_dataset_files(self):
        correct = ['archive.zip']
        files = self.dataset_reader.get_dataset_files()
        self.assertEqual(files, correct)
        self.assertEqual(len(files), 1)

    def test_read_dataset(self):
        correct = ['Blair to face MPs amid feud talk\n\n'
           'Tony Blair faces his first prime minister\'s questions of 2005 after a week of renewed speculation about his '
           'relationship with Gordon Brown.\n\n'
           'Meanwhile, the chancellor is leaving Britain on a high-profile tour of Africa to highlight poverty issues. '
           'But before doing so, he insisted he still trusted Mr Blair, despite claims to the contrary in a new book. '
           'Labour MPs have warned against disunity and Tory leader Michael Howard may well take up the theme in the '
           'Commons. The Tories have already accused the prime minister and his chancellor of behaving like "schoolboys '
           'squabbling in a playground".\n\n'
           'Michael Howard is likely to want to capitalise further on the spat when he goes head-to-head with the '
           'prime minister in the Commons. At a campaign poster launch on Tuesday, Mr Brown was joined by Alan Milburn, '
           'who Mr Blair controversially put in charge of election planning in place of the chancellor.\n\n'
           'Later this week the prime minister is due to set out the themes of his party\'s next election manifesto, '
           'which for the past two polls have been drawn up by the chancellor. Mr Brown, meanwhile, is visiting Tanzania, '
           'Mozambique and Kenya to highlight the plight of many Africans hit by Aids, war and famine - issues which '
           'Mr Blair has also spoken out on. The prime minister and chancellor faced backbench discontent at Monday\'s '
           'meeting of the Parliamentary Labour Party over claims made in journalist Robert Peston\'s new book. '
           'Mr Blair told MPs and peers: "I know from everyone here, in Cabinet and government, nothing is going to get '
           'in the way of a unified Labour Party with a unified position and winning the third term people desperately '
           'need." Labour\'s Paul Flynn said the pair had had a "scorching" from MPs.\n\n'
           'On Tuesday, Deputy Prime Minister Mr Prescott told BBC News: "They told us very clearly, it was the troops '
           'telling the leaders: get in line." The new book claims Mr Prescott hosted a dinner in November 2003 where '
           'the prime minister told Mr Brown he would stand down before the next election because he had lost trust '
           'over the Iraq war. Mr Blair then changed his mind in June 2004, after Cabinet allies intervened and amid '
           'suspicion the chancellor was manoeuvring against him, writes Mr Peston. In Mr Peston\'s book Mr Brown '
           'is alleged to have told the prime minister: "There is nothing you could ever say to me now that I could '
           'ever believe."\n']
        texts = self.dataset_reader.read_dataset('archive.zip')
        not_found = self.dataset_reader.read_dataset('test.zip')
        self.assertEqual(texts[0:1], correct)
        self.assertEqual(len(texts), 2224)
        self.assertEqual(not_found, False)

    def test_clear_inputs(self):
        input_text1 = 'Meanwhile, the chancellor is leaving Britain on a high-profile tour of Africa to highlight poverty issues.'
        self.dataset_reader.clear_inputs()
        texts0 = self.dataset_reader.read_user_input()
        self.dataset_reader.input_article(input_text1)
        texts1 = self.dataset_reader.read_user_input()
        self.dataset_reader.clear_inputs()
        self.assertEqual(texts0, [])
        self.assertEqual(texts1, ['Meanwhile, the chancellor is leaving Britain on a high-profile tour of Africa to highlight poverty issues.'])

    def test_input_article(self):
        input_text1 = 'Meanwhile, the chancellor is leaving Britain on a high-profile tour of Africa to highlight poverty issues.'
        input_text2 = 'over the Iraq war. Mr Blair then changed his mind in June 2004, after Cabinet allies intervened and amid'
        self.dataset_reader.clear_inputs()
        self.dataset_reader.input_article(input_text1)
        self.dataset_reader.input_article(input_text2)
        returned_texts = self.dataset_reader.read_user_input()
        self.dataset_reader.clear_inputs()
        self.assertEqual(returned_texts, ['Meanwhile, the chancellor is leaving Britain on a high-profile '
                                          'tour of Africa to highlight poverty issues.',
                                          'over the Iraq war. Mr Blair then changed his mind in June 2004, '
                                          'after Cabinet allies intervened and amid'])

class LanguageCodes(object):
    bengali = 'bn'
    gujarati = 'gu'
    hindi = 'hi'
    kannada = 'kn'
    malyalam = 'ml'
    marathi = 'mr'
    nepali = 'ne'
    odia = 'or'
    panjabi = 'pa'
    sanskrit = 'sa'

    def get_all_language_codes(self):
        return [self.bengali, self.gujarati, self.hindi,
                self.kannada, self.malyalam, self.marathi,
                self.nepali, self.odia, self.panjabi, self.sanskrit]


class LMConfigs(object):
    all_language_codes = LanguageCodes()
    lm_model_file_url = {
        all_language_codes.bengali: 'https://www.dropbox.com/s/4berhstpw836kcw/export.pkl?raw=1',
        all_language_codes.gujarati: 'https://www.dropbox.com/s/6ldfcs35tw2fan3/export.pkl?raw=1',
        all_language_codes.hindi: 'https://www.dropbox.com/s/sakocwz413eyzt6/export.pkl?raw=1',
        all_language_codes.kannada: 'https://www.dropbox.com/s/h04gp20t59gv4ra/export.pkl?raw=1',
        all_language_codes.malyalam: 'https://www.dropbox.com/s/laj4dd0tivquw3d/export.pkl?raw=1',
        all_language_codes.marathi: 'https://www.dropbox.com/s/o1582btk32pk7tk/export.pkl?raw=1',
        all_language_codes.nepali: 'https://www.dropbox.com/s/koxiy7l3zbkgzn6/export.pkl?raw=1',
        all_language_codes.odia: 'https://www.dropbox.com/s/dl3t6sp8p3ifp4q/export.pkl?raw=1',
        all_language_codes.panjabi: 'https://www.dropbox.com/s/ejiv5pdsi2mhhxa/export.pkl?raw=1',
        all_language_codes.sanskrit: 'https://www.dropbox.com/s/4ay1by5ryz6k39l/sanskrit_export.pkl?raw=1'
    }
    tokenizer_model_file_url = {
        all_language_codes.bengali: 'https://www.dropbox.com/s/29h7vqme1kb8pmw/bengali_lm.model?raw=1',
        all_language_codes.gujarati: 'https://www.dropbox.com/s/8ivj97gaprhq5pv/gujarati_lm.model?raw=1',
        all_language_codes.hindi: 'https://www.dropbox.com/s/xrsjt8zbhwo7zxq/hindi_lm.model?raw=1',
        all_language_codes.kannada: 'https://www.dropbox.com/s/m8qlc3wgw1m8ggp/kannada_lm.model?raw=1',
        all_language_codes.malyalam: 'https://www.dropbox.com/s/2lqbb93tzz8vb8a/malyalam_lm.model?raw=1',
        all_language_codes.marathi: 'https://www.dropbox.com/s/nnq9erkr9z49th7/marathi_lm.model?raw=1',
        all_language_codes.nepali: 'https://www.dropbox.com/s/kmpc8i3c3n0if23/nepali_lm.model?raw=1',
        all_language_codes.odia: 'https://www.dropbox.com/s/1xnibv1sytgt9ci/oriya_lm.model?raw=1',
        all_language_codes.panjabi: 'https://www.dropbox.com/s/jxwr9ytn0zfzulc/panjabi_lm.model?raw=1',
        all_language_codes.sanskrit: 'https://www.dropbox.com/s/e13401nsekulq17/tokenizer.model?raw=1'
    }

    def __init__(self, language_code: str):
        self.language_code = language_code

    def get_config(self):
        return {
            'lm_model_url': self.lm_model_file_url[self.language_code],
            'lm_model_file_name': 'export.pkl',
            'tokenizer_model_url': self.tokenizer_model_file_url[self.language_code],
            'tokenizer_model_file_name': 'tokenizer.model'
        }

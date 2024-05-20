from .abstract_class import Saver
import json

BASE_PATH = 'data/vacancies.json'


class JSONSaver(Saver):
    def __init__(self, path=BASE_PATH):
        self.__path = path

    def __repr__(self):
        return f'Path: {self.__path}'
    
    def get_path(self) -> str:
        """
        Get the path of the JSON file.

        Returns:
            str: The path of the JSON file.
        """
        return self.__path

    def save(self, data):
        """
        Save the given data to a JSON file.

        Parameters:
            data (Any): The data json to be saved.
        """
        try:
            with open(self.__path, 'w') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.close()
        except FileNotFoundError:
            raise FileNotFoundError(f'File not found: {self.__path}')

    def delete(self, id=""):
        """
        Deletes a record from a JSON file based on the provided ID.

        Parameters:
            id (int): The ID of the record to be deleted optional.

        Returns:
            None

        This function opens the JSON file specified by the `path` attribute, reads its contents, and filters out the record with the specified ID. 
        The filtered data is then written back to the JSON file, overwriting the original content.

        Note:
            - The JSON file is assumed to contain a list of records, where each record is a dictionary with an 'id' key.
            - The function assumes that the JSON file is encoded in UTF-8.
            - The function does not handle any exceptions that may occur during the file operations.

        """

        # Читаем данные из JSON
        try:
            with open(self.__path, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f'File not found: {self.__path}')

        if id is not "":
             # Если в поле id нет нужного значения, то ничего не делаем, иначе не добавляем в новый список
            data = [record for record in data if record.get('id') != id]
        else: 
            data = []
       
        # Записываем данные в JSON
        try: 
            with open(self.__path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
                file.close()
        except FileNotFoundError:
            raise FileNotFoundError(f'File not found: {self.__path}')


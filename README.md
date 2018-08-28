# FileCase - Lossless File Compression Using Huffman Coding and Encryption Through AES-256
> Written by Lewis Kim

### Description

FileCase is a lightweight desktop application written in Python for lossless compression or AES-256 CFB encryption of ``.txt`` and ``.docx`` files. If a file is compressed, the ``HuffmanCoder`` object instance that compressed the file (which contains the Huffman Coding Tree) is serialized into a pickle file inside ``FileCase/app/data`` following a very specific directory structure for data peristence, and the user only needs to worry about the compressed ``.bin`` file, without having to keep track of both the compressed file and a file containing the Huffman Coding Tree.

If a file is encrypted instead, the user-given password to encrypt the file is not stored or serialized anywhere; it is up to the user to remember and keep track of the password. The encrypted data is written to a ``.bin`` file, and once decrypted it will be re-written into a ``.txt`` or ``.docx`` file, depending on the original file extention.

In both cases, to maintain data persistence, the compressed/encrypted files' names cannot be changed, or the application will not be able to properly decompress/decrypt.

The Huffman Coding Algorithm drastically reduces file sizes (up to 50% for ``.txt`` files, and up to 67% for ``.docx`` files): inside the ``test`` folder, you can see an uncompressed ``.docx`` file named ``test-para.docx``, which has about a page of text and has a size of 16KB. The compressed version of the file, `test-para-docx.bin`, holds only 4KB, while maintaining all the information present in the original file.

Encrypted files are not compressed, as there would be very little meaning to compressing a properly encrypted file (lack of statistical patterns for compression).

For a walkthrough of FileCase and its GUI, [click here.](gui_sample/README.md)

### Installation

FileCase was written in Python 3.6, and will not work with Python 2.

Required packages:
- ``tkinter`` (``pip3 install tkinter``)
- ``bitstring`` (``pip3 install bitstring``)
- ``bitarray`` (``pip3 install bitarray``)
- ``python-docx`` (``pip3 install python-docx``)
- ``heapq`` (part of the Python library)
- ``pycrypto`` (``pip3 install pycrypto``)

To run this application, go inside the ``FileCase`` directory, and run the following command:

``python3 run.py``

and the application is ready for use. FileCase will maintain a directory structure for compressed/encrypted files within itself, and the user only needs to worry about properly storing the compressed/decompressed ``.bin`` files, without changing its names.

### References

References to the libraries and packages used in FileCase:

1) ``tkinter``: https://wiki.python.org/moin/TkInter
2) ``bitstring``: https://pypi.org/project/bitstring/
3) ``bitarray``: https://pypi.org/project/bitarray/
4) ``python-docx``: https://python-docx.readthedocs.io/en/latest/
5) ``heapq``: https://docs.python.org/3.0/library/heapq.html
6) ``pycrypto``: https://pypi.org/project/pycrypto/

# Menu options based on the language
features_dict = {
    "English": [
        {
            "feat_id": "scheme_support",
            "feat_name": "Information Center (Schemes & Support)",
        },
        {
            "feat_id": "krishi_pathshala",
            "feat_name": "Krishi Pathshala (Agriculture School)",
        },
        {"feat_id": "doc_decoder", "feat_name": "Document Decoder"},
    ],
    "हिंदी": [
        {"feat_id": "scheme_support", "feat_name": "जानकारी एक्सेस (योजनाएं और समर्थन)"},
        {"feat_id": "krishi_pathshala", "feat_name": "कृषि पाठशाला"},
        {"feat_id": "doc_decoder", "feat_name": "दस्तावेज़ डिकोडर"},
    ],
    "বাংলা": [
        {"feat_id": "scheme_support", "feat_name": "তথ্য অ্যাক্সেস (योजना এবং সহায়তা)"},
        {"feat_id": "krishi_pathshala", "feat_name": "কৃষি পাঠশালা"},
        {"feat_id": "doc_decoder", "feat_name": "ডকুমেন্ট ডিকোডার"},
    ],
    "मराठी": [
        {"feat_id": "scheme_support", "feat_name": "माहिती प्रवेश (योजना आणि सहाय्य)"},
        {"feat_id": "krishi_pathshala", "feat_name": "कृषी पाठशाळा"},
        {"feat_id": "doc_decoder", "feat_name": "डॉक्युमेंट डिकोडर"},
    ],
}

# Supported languages
supported_languages = ["English", "हिंदी", "বাংলা", "मराठी"]


footer_content = {
    #   English content
    "English": """
# About Kisan Sahayak

**Kisan Sahayak** is your digital companion for all things agriculture. 

We provide:

* **Easy access to information:** Learn about government schemes, connect with helpful organizations, and get expert advice.
* **Educational resources:**  Explore modern farming techniques and improve your skills.
* **Document assistance:**  Understand complex legal documents and protect yourself from fraud.

**Our mission** is to empower farmers with knowledge and technology, helping them thrive in the ever-evolving world of agriculture.
    """,
    #   Hindi content
    "हिंदी": """
# किसान सहायक के बारे में

**किसान सहायक** खेतीबाड़ी से जुड़ी सभी चीजों के लिए आपका डिजिटल साथी है।

हम प्रदान करते हैं:

* **जानकारी तक आसान पहुँच:** सरकारी योजनाओं के बारे में जानें, सहायक संगठनों से जुड़ें, और विशेषज्ञों की सलाह लें।
* **दस्तावेज़ सहायता:** जटिल कानूनी दस्तावेज़ों को समझें और खुद को धोखाधड़ी से बचाएं।
* **शैक्षिक संसाधन:** आधुनिक खेती तकनीकों का अन्वेषण करें और अपने कौशल में सुधार करें।

**हमारा मिशन** किसानों को ज्ञान और तकनीक से सशक्त बनाना है, जिससे उन्हें कृषि की लगातार विकसित हो रही दुनिया में सफलता प्राप्त हो सके।
    """,
    #   Bengali content
    "বাংলা": """
# কৃষক সহায়ক সম্পর্কে

**কৃষক সহায়ক** হল কৃষিকাজের সবকিছুর জন্য আপনার ডিজিটাল সঙ্গী।

আমরা প্রদান করি:

* **তথ্যে সহজ पहुँच:** সরকারি প্রকল্প সম্পর্কে জানুন, সহায়ক সংস্থাগুলির সাথে যোগাযোগ করুন এবং বিশেষজ্ঞদের পরামর্শ নিন।
* **ডকুমেন্ট সহায়তা:** জটিল আইনি নথিগুলি বুঝুন এবং নিজেকে জালিয়াতি থেকে রক্ষা করুন।
* **শিক্ষাগত সংস্থান:** আধুনিক কৃষি কৌশলগুলি অন্বेषণ করুন এবং আপনার দক্ষতা উন্নত করুন।

**আমাদের লক্ষ্য** হল কৃষকদের জ্ঞান এবং প্রযুক্তি দিয়ে ক্ষমতায়িত করা, কৃষির ক্রমবর্ধমান বিশ্বে তাদের উন্নতি করতে সাহায্য করা।
    """,
    #   Marathi content
    "मराठी": """
# किसान सहाय्यक बद्दल

**किसान सहाय्यक** ही शेतीसाठी तुमची डिजिटल सोबती आहे.

आम्ही प्रदान करतो:

* **सुलभ माहिती प्रवेश:** सरकारी योजना जाणून घ्या, उपयोगी संस्थांशी संपर्क साधा, आणि तज्ञांचा सल्ला मिळवा.
* **शैक्षणिक साधने:** आधुनिक शेती तंत्रे शोधा आणि तुमचे कौशल्य वाढवा.
* **दस्तऐवज सहाय्य:** गुंतागुंतीचे कायदेशीर दस्तऐवज समजून घ्या आणि फसवणुकीपासून स्वतःचे रक्षण करा.

**आमचे उद्दिष्ट** म्हणजे शेतकऱ्यांना ज्ञान आणि तंत्रज्ञानाच्या साहाय्याने सक्षम करणे, जेणेकरून ते शेतीतील सतत बदलणाऱ्या जगात यशस्वी होऊ शकतील.
""",
}

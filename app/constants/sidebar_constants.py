# Menu options based on the language
features_dict = {
    "English": [
        {"feat_id": "scheme_support", "feat_name": "Information Access (Schemes & Support)"},
        {"feat_id": "doc_decoder", "feat_name": "Document Decoder"},
        {"feat_id": "ask_kisan", "feat_name": "Ask Kisan Sahayak"},
        {
            "feat_id": "krishi_pathshala",
            "feat_name": "Krishi Pathshala (Agriculture School)",
        },
    ],
    "हिंदी": [
        {"feat_id": "scheme_support", "feat_name": "जानकारी एक्सेस (योजनाएं और समर्थन)"},
        {"feat_id": "doc_decoder", "feat_name": "दस्तावेज़ डिकोडर"},
        {"feat_id": "ask_kisan", "feat_name": "किसान सहायक से पूछें"},
        {"feat_id": "krishi_pathshala", "feat_name": "कृषि पाठशाला"},
    ],
    "বাংলা": [
        {"feat_id": "scheme_support", "feat_name": "তথ্য অ্যাক্সেস (योजना এবং সহায়তা)"},
        {"feat_id": "doc_decoder", "feat_name": "ডকুমেন্ট ডিকোডার"},
        {"feat_id": "ask_kisan", "feat_name": "কৃষক সহায়ককে জিজ্ঞাসা করুন"},
        {"feat_id": "krishi_pathshala", "feat_name": "কৃষি পাঠশালা"},
    ],
}

# Supported languages
supported_languages = [
    "English",
    "हिंदी",
    "বাংলা",
]


footer_content = {
    "English": """
# About Kisan Sahayak

**Kisan Sahayak** is your digital companion for all things agriculture. 

We provide:

* **Easy access to information:** Learn about government schemes, connect with helpful organizations, and get expert advice.
* **Smart crop recommendations:**  Receive personalized crop suggestions based on your soil and local weather.
* **Document assistance:**  Understand complex legal documents and protect yourself from fraud.
* **Educational resources:**  Explore modern farming techniques and improve your skills.

**Our mission** is to empower farmers with knowledge and technology, helping them thrive in the ever-evolving world of agriculture.
    """,
    "हिंदी": """
# किसान सहायक के बारे में

**किसान सहायक** खेतीबाड़ी से जुड़ी सभी चीजों के लिए आपका डिजिटल साथी है।

हम प्रदान करते हैं:

* **जानकारी तक आसान पहुँच:** सरकारी योजनाओं के बारे में जानें, सहायक संगठनों से जुड़ें, और विशेषज्ञों की सलाह लें।
* **स्मार्ट फसल सुझाव:** अपनी मिट्टी और स्थानीय मौसम के आधार पर व्यक्तिगत फसल सुझाव प्राप्त करें।
* **दस्तावेज़ सहायता:** जटिल कानूनी दस्तावेज़ों को समझें और खुद को धोखाधड़ी से बचाएं।
* **शैक्षिक संसाधन:** आधुनिक खेती तकनीकों का अन्वेषण करें और अपने कौशल में सुधार करें।

**हमारा मिशन** किसानों को ज्ञान और तकनीक से सशक्त बनाना है, जिससे उन्हें कृषि की लगातार विकसित हो रही दुनिया में सफलता प्राप्त हो सके।
    """,
    "বাংলা": """
# কৃষক সহায়ক সম্পর্কে

**কৃষক সহায়ক** হল কৃষিকাজের সবকিছুর জন্য আপনার ডিজিটাল সঙ্গী।

আমরা প্রদান করি:

* **তথ্যে সহজ पहुँच:** সরকারি প্রকল্প সম্পর্কে জানুন, সহায়ক সংস্থাগুলির সাথে যোগাযোগ করুন এবং বিশেষজ্ঞদের পরামর্শ নিন।
* **স্মার্ট ফসলের পরামর্শ:** আপনার মাটি এবং স্থানীয় আবহাওয়ার উপর ভিত্তি করে ব্যক্তিগতকৃত ফসলের পরামর্শ পান।
* **ডকুমেন্ট সহায়তা:** জটিল আইনি নথিগুলি বুঝুন এবং নিজেকে জালিয়াতি থেকে রক্ষা করুন।
* **শিক্ষাগত সংস্থান:** আধুনিক কৃষি কৌশলগুলি অন্বेषণ করুন এবং আপনার দক্ষতা উন্নত করুন।

**আমাদের লক্ষ্য** হল কৃষকদের জ্ঞান এবং প্রযুক্তি দিয়ে ক্ষমতায়িত করা, কৃষির ক্রমবর্ধমান বিশ্বে তাদের উন্নতি করতে সাহায্য করা।
    """,
}

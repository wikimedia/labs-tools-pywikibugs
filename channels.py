channels = {
    "#huggle":
        lambda x: x.get("X-Bugzilla-Product", None) == "Huggle",
    "#pywikibot":
        lambda x: x.get("X-Bugzilla-Product", None) == "Pywikibot",
    "#wikimedia-corefeatures":
        lambda x: (x.get("X-Bugzilla-Product", None) == "MediaWiki extensions") and \
                  (x.get("X-Bugzilla-Component", None) in ["Echo", "Flow", "PageCuration", "Thanks", "WikiLove"]),
    "#mediawiki-i18n":
        lambda x: (x.get("X-Bugzilla-Component", None) in ["ContentTranslation"]),
    "#wikimedia-labs":
        lambda x: x.get("X-Bugzilla-Product", None) in ["Tool Labs tools", "Wikimedia Labs"],
    "#wikimedia-mobile":
        lambda x: x.get("X-Bugzilla-Product", None) in ["Wikimedia Mobile", "Commons App", "Wikipedia App", "MobileFrontend"],
    "#wikimedia-qa":
        lambda x: (x.get("X-Bugzilla-Product", None) == "Wikimedia") and \
                  (x.get("X-Bugzilla-Component", None) in ["Continuous integration", "Quality Assurance"]),
    "#mediawiki-visualeditor":
        lambda x: x.get("X-Bugzilla-Product", None) in ["VisualEditor", "OOjs", "OOjs UI"] or \
                  (
                      (x.get("X-Bugzilla-Product", None) == "MediaWiki extensions") and \
                      (x.get("X-Bugzilla-Component", None) in ["TemplateData"])
                  ),
    "#mediawiki-parsoid":
        lambda x: x.get("X-Bugzilla-Product", None) in ["Parsoid"],
    "#wikimedia-multimedia":
        lambda x: \
            (
                x.get("X-Bugzilla-Product", None) in ["MediaWiki extensions"] and
                x.get("X-Bugzilla-Component", None) in
                    ["UploadWizard", "TimedMediaHandler", "VipsScaler", "GlobalUsage", "MultimediaViewer", "GWToolset",
                     "Score", "PagedTiffHandler", "PdfHandler", "ImageMap", "CommonsMetadata", "OggHandler"]
            ) or \
            (
                x.get("X-Bugzilla-Product", None) in ["MediaWiki"] and
                x.get("X-Bugzilla-Component", None) in
                    ["File management", "Uploading"]
            ),
    "#wikimedia-growth":
        lambda x:
            (
                x.get("X-Bugzilla-Product", None) in ["MediaWiki extensions"] and
                x.get("X-Bugzilla-Component", None) in ["GuidedTour", "GettingStarted"]
            )
}

default_channel = "#wikimedia-dev"
firehose_channel = "#mediawiki-feed"

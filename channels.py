channels = {
    "#huggle":
        lambda x: x.get("X-Bugzilla-Product", None) == "Huggle",
    "#pywikibot":
        lambda x: x.get("X-Bugzilla-Product", None) == "Pywikibot",
    "#wikidata":
        lambda x: \
            (
                x.get("X-Bugzilla-Product", None) in ["MediaWiki extensions"] and
                x.get("X-Bugzilla-Component", None) in
                    ["WikidataRepo", "WikidataClient"]
            ) or \
            (
                x.get("X-Bugzilla-Product", None) in ["Wikimedia"] and
                x.get("X-Bugzilla-Component", None) in
                    ["Wikidata"]
            ),
    "#wikimedia-corefeatures":
        lambda x: (x.get("X-Bugzilla-Product", None) == "MediaWiki extensions") and \
                  (x.get("X-Bugzilla-Component", None) in ["Echo", "Flow", "PageCuration", "Thanks", "WikiLove"]),
    "#mediawiki-i18n":
        lambda x: (x.get("X-Bugzilla-Component", None) in ["ContentTranslation"]),
    "#wikimedia-labs":
        lambda x: x.get("X-Bugzilla-Product", None) in ["Tool Labs tools", "Wikimedia Labs"] or \
                  (
                   (x.get("X-Bugzilla-Product", None) == "MediaWiki extensions") and \
                   (x.get("X-Bugzilla-Component", None) in ["OpenStackManager"])
                  ),
    "#wikimedia-mobile":
        lambda x: x.get("X-Bugzilla-Product", None) in ["Wikimedia Mobile", "Commons App", "Wikipedia App", "MobileFrontend"],
    "#wikimedia-qa":
        lambda x: (
                      (x.get("X-Bugzilla-Product", None) == "Wikimedia") and \
                      (x.get("X-Bugzilla-Component", None) in ["Continuous integration", "Quality Assurance"])
                  ) or \
                  (
                      (x.get("X-Bugzilla-Product", None) == "Wikimedia Labs") and \
                      (x.get("X-Bugzilla-Component", None) == "deployment-prep (beta)")
                  ),
    "#mediawiki-visualeditor":
        lambda x: x.get("X-Bugzilla-Product", None) in ["VisualEditor", "OOjs", "OOjs UI"] or \
                  (
                      (x.get("X-Bugzilla-Product", None) == "MediaWiki extensions") and \
                      (x.get("X-Bugzilla-Component", None) in ["TemplateData", "Cite", "WikiEditor"])
                  ) or \
                  (
                      (x.get("X-Bugzilla-Product", None) == "MediaWiki") and \
                      (x.get("X-Bugzilla-Component", None) in ["Page editing", "ResourceLoader"])
                  ),
    "#mediawiki-parsoid":
        lambda x: x.get("X-Bugzilla-Product", None) in ["Parsoid"],
    "#wikimedia-multimedia":
        lambda x: \
            (
                x.get("X-Bugzilla-Product", None) in ["MediaWiki extensions"] and
                x.get("X-Bugzilla-Component", None) in
                    ["UploadWizard", "TimedMediaHandler", "VipsScaler", "GlobalUsage", "MultimediaViewer", "GWToolset",
                     "Score", "PagedTiffHandler", "PdfHandler", "ImageMap", "CommonsMetadata", "OggHandler",
                     "ImageMetrics"]
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
            ),
    "#wikimedia-analytics":
        lambda x: x.get("X-Bugzilla-Product", None) == "Analytics",

    # The following changes should ALWAYS be in #wikimedia-dev, even if the bugs
    # are also reported elsewhere.
    "#wikimedia-dev":
        lambda x: x.get("X-Bugzilla-Product", None) == "MediaWiki"
}

default_channel = "#wikimedia-dev"
firehose_channel = "#mediawiki-feed"

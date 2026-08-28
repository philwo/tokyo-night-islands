plugins {
    id("org.jetbrains.intellij.platform") version "2.18.1"
}

group = "de.philwo"
version = "0.6.0"

repositories {
    mavenCentral()
    intellijPlatform {
        defaultRepositories()
    }
}

dependencies {
    intellijPlatform {
        intellijIdea("2025.3") {
            useInstaller = false
        }
    }
}

intellijPlatform {
    buildSearchableOptions = false
    pluginConfiguration {
        ideaVersion {
            sinceBuild = "253"
            untilBuild = provider { null }
        }
    }
    pluginVerification {
        ides {
            recommended()
        }
    }
}

tasks.jar {
    from(listOf("LICENSE", "NOTICE")) {
        into("META-INF")
    }
}

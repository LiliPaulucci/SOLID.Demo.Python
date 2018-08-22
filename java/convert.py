import translators
import converters
import sys
import dependency_injector.providers as providers


if len(sys.argv) < 2:
    print('usage: %s <number>' % sys.argv[0])
    sys.exit(1)


number = sys.argv[1]


# Define abstract cache client factory:
translator_factory = providers.AbstractFactory(translators.ITranslator)

converter_factory = providers.AbstractFactory(converters.INumeralConverter)

if __name__ == '__main__':
    # Override abstract factory with CardinalTranslator factory:
    translator_factory.override(providers.Factory(translators.CardinalTranslator))
    translator = translator_factory()

    converter_factory.override(providers.Factory(converters.ArabicToCardinalConverter, translator=translator))
    arabic_to_cardinal = converter_factory()
    print(arabic_to_cardinal.convert(str(number)))

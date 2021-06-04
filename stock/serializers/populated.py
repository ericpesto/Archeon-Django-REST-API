from stock_activities.serializers.common import StockActivitySerializer
from stock_links.serializers.common import StockLinkSerializer
from categories.serializers.common import CategorySerializer
from names.serializers.common import NameSerializer
from ..serializers.common import StockSerializer

class PopulatedStockSerializer(StockSerializer):

    stock_activities = StockActivitySerializer(many=True)
    stock_links = StockLinkSerializer(many=True)
    category_id = CategorySerializer()
    sub_category_1_id = CategorySerializer()
    sub_category_2_id = CategorySerializer()
    artist_id = NameSerializer()
    location_id = NameSerializer()
    source_id = NameSerializer()
    buyer_id = NameSerializer()
    partner_id = NameSerializer()